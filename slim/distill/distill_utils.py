<<<<<<< HEAD
# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
=======
# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
>>>>>>> PaddlePaddle-release/2.4
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import time
from collections import deque
import shutil

import paddle
from paddle.distributed import fleet
import paddle.nn.functional as F

<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
from paddleseg.utils import TimeAverager, calculate_eta, resume, logger, worker_init_fn
from paddleseg.core.val import evaluate
from paddleseg.models.losses import DistillCrossEntropyLoss
=======
from paddleseg.utils import (TimeAverager, calculate_eta, resume, logger,
                             worker_init_fn, train_profiler, op_flops_funs)
from .val import evaluate
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
from paddleseg.utils import TimeAverager, calculate_eta, resume, logger, worker_init_fn
from paddleseg.core.val import evaluate
from paddleseg.models.losses import DistillCrossEntropyLoss
>>>>>>> PaddlePaddle-release/2.4


def check_logits_losses(logits_list, losses):
    len_logits = len(logits_list)
    len_losses = len(losses['types'])
    if len_logits != len_losses:
        raise RuntimeError(
            'The length of logits_list should equal to the types of loss config: {} != {}.'
            .format(len_logits, len_losses))


def loss_computation(logits_list, labels, losses, edges=None):
    check_logits_losses(logits_list, losses)
    loss_list = []
    for i in range(len(logits_list)):
        logits = logits_list[i]
        loss_i = losses['types'][i]
        # Whether to use edges as labels According to loss type.
        if loss_i.__class__.__name__ in ('BCELoss',
                                         'FocalLoss') and loss_i.edge_label:
            loss_list.append(losses['coef'][i] * loss_i(logits, edges))
        elif loss_i.__class__.__name__ in ("KLLoss", ):
            loss_list.append(losses['coef'][i] * loss_i(
                logits_list[0], logits_list[1].detach()))
        else:
            loss_list.append(losses['coef'][i] * loss_i(logits, labels))
    return loss_list


<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
=======
>>>>>>> PaddlePaddle-release/2.4
def distill_loss_computation(student_logits_list,
                             teacher_logits_list,
                             labels,
                             losses,
                             edges=None):
    assert len(student_logits_list) == len(teacher_logits_list)
    check_logits_losses(student_logits_list, losses)

    loss_list = []
    for i in range(len(student_logits_list)):
        s_logits = student_logits_list[i]
        t_logits = teacher_logits_list[i]
        loss_i = losses['types'][i]
        loss_list.append(losses['coef'][i] * loss_i(s_logits, t_logits, labels))
    return loss_list


def distill_train(distill_model,
                  train_dataset,
                  val_dataset=None,
                  optimizer=None,
                  save_dir='output',
                  iters=10000,
                  batch_size=2,
                  resume_model=None,
                  save_interval=1000,
                  log_iters=10,
                  num_workers=0,
                  use_vdl=False,
                  losses=None,
                  distill_losses=None,
                  keep_checkpoint_max=5,
                  test_config=None,
                  fp16=False):
<<<<<<< HEAD
=======
def train(model,
          train_dataset,
          val_dataset=None,
          optimizer=None,
          save_dir='output',
          iters=10000,
          batch_size=2,
          resume_model=None,
          save_interval=1000,
          log_iters=10,
          num_workers=0,
          use_vdl=False,
          losses=None,
          keep_checkpoint_max=5,
          test_config=None,
          fp16=False,
          profiler_options=None):
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
>>>>>>> PaddlePaddle-release/2.4
    """
    Launch training.

    Args:
        distill_model (nn.Layer): A distill model.
        train_dataset (paddle.io.Dataset): Used to read and process training datasets.
        val_dataset (paddle.io.Dataset, optional): Used to read and process validation datasets.
        optimizer (paddle.optimizer.Optimizer): The optimizer.
        save_dir (str, optional): The directory for saving the model snapshot. Default: 'output'.
        iters (int, optional): How may iters to train the model. Defualt: 10000.
        batch_size (int, optional): Mini batch size of one gpu or cpu. Default: 2.
        resume_model (str, optional): The path of resume model.
        save_interval (int, optional): How many iters to save a model snapshot once during training. Default: 1000.
        log_iters (int, optional): Display logging information at every log_iters. Default: 10.
        num_workers (int, optional): Num workers for data loader. Default: 0.
        use_vdl (bool, optional): Whether to record the data to VisualDL during training. Default: False.
<<<<<<< HEAD
        losses (dict, optional): A dict including 'types' and 'coef'. The length of coef should equal to 1 or len(losses['types']).
=======
        losses (dict): A dict including 'types' and 'coef'. The length of coef should equal to 1 or len(losses['types']).
>>>>>>> PaddlePaddle-release/2.4
            The 'types' item is a list of object of paddleseg.models.losses while the 'coef' item is a list of the relevant coefficient.
        distill_losses (dict): A dict including 'types' and 'coef'. The format of distill_losses is the same as losses.
        keep_checkpoint_max (int, optional): Maximum number of checkpoints to save. Default: 5.
        test_config(dict, optional): Evaluation config.
<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
        fp16 (bool, optional): Whether to use amp. Not support for now.
=======
        fp16 (bool, optional): Whether to use amp.
        profiler_options (str, optional): The option of train profiler.
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
        fp16 (bool, optional): Whether to use amp. Not support for now.
>>>>>>> PaddlePaddle-release/2.4
    """
    if fp16:
        raise RuntimeError("Distillation doesn't support amp training.")

    nranks = paddle.distributed.ParallelEnv().nranks
    local_rank = paddle.distributed.ParallelEnv().local_rank
    student_model = distill_model._student_models

    start_iter = 0
    if resume_model is not None:
        start_iter = resume(student_model, optimizer, resume_model)

    if not os.path.isdir(save_dir):
        if os.path.exists(save_dir):
            os.remove(save_dir)
        os.makedirs(save_dir)

    if nranks > 1:
<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
=======
>>>>>>> PaddlePaddle-release/2.4
        strategy = fleet.DistributedStrategy()
        strategy.find_unused_parameters = True
        fleet.init(is_collective=True, strategy=strategy)

        optimizer = fleet.distributed_optimizer(
            optimizer)  # The return is Fleet object
        ddp_distill_model = fleet.distributed_model(distill_model)
<<<<<<< HEAD
=======
        paddle.distributed.fleet.init(is_collective=True)
        optimizer = paddle.distributed.fleet.distributed_optimizer(
            optimizer)  # The return is Fleet object
        ddp_model = paddle.distributed.fleet.distributed_model(model)
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
>>>>>>> PaddlePaddle-release/2.4

    batch_sampler = paddle.io.DistributedBatchSampler(
        train_dataset, batch_size=batch_size, shuffle=True, drop_last=True)

    loader = paddle.io.DataLoader(
        train_dataset,
        batch_sampler=batch_sampler,
        num_workers=num_workers,
        return_list=True,
        worker_init_fn=worker_init_fn,
    )

<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
=======
    # use amp
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
>>>>>>> PaddlePaddle-release/2.4
    if fp16:
        logger.info('use amp to train')
        scaler = paddle.amp.GradScaler(init_loss_scaling=1024)

    if use_vdl:
        from visualdl import LogWriter
        log_writer = LogWriter(save_dir)

    avg_loss = 0.0
    avg_out_loss = 0.0
    avg_out_distill_loss = 0.0
    avg_feature_distill_loss = 0.0
    avg_out_loss_list = []
    iters_per_epoch = len(batch_sampler)
<<<<<<< HEAD
    best_acc = -1.0
=======
    best_mean_iou = -1.0
>>>>>>> PaddlePaddle-release/2.4
    best_model_iter = -1
    reader_cost_averager = TimeAverager()
    batch_cost_averager = TimeAverager()
    save_models = deque()
    batch_start = time.time()

    iter = start_iter
    while iter < iters:
        for data in loader:
            iter += 1
            if iter > iters:
<<<<<<< HEAD
                version = paddle.__version__
                if version == '2.1.2':
                    continue
                else:
                    break
=======
                break
>>>>>>> PaddlePaddle-release/2.4
            reader_cost_averager.record(time.time() - batch_start)
            images = data[0]
            labels = data[1].astype('int64')
            edges = None
            if len(data) == 3:
                edges = data[2].astype('int64')
<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
            if hasattr(distill_model,
                       'data_format') and distill_model.data_format == 'NHWC':
=======
            if hasattr(model, 'data_format') and model.data_format == 'NHWC':
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
            if hasattr(distill_model,
                       'data_format') and distill_model.data_format == 'NHWC':
>>>>>>> PaddlePaddle-release/2.4
                images = images.transpose((0, 2, 3, 1))

            if fp16:
                with paddle.amp.auto_cast(
                        enable=True,
                        custom_white_list={
                            "elementwise_add", "batch_norm", "sync_batch_norm"
                        },
                        custom_black_list={'bilinear_interp_v2'}):
                    if nranks > 1:
<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
                        logits_list = ddp_distill_model(images)
                    else:
                        logits_list = distill_model(images)
=======
                        logits_list = ddp_model(images)
                    else:
                        logits_list = model(images)
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
                        logits_list = ddp_distill_model(images)
                    else:
                        logits_list = distill_model(images)
>>>>>>> PaddlePaddle-release/2.4
                    loss_list = loss_computation(
                        logits_list=logits_list,
                        labels=labels,
                        losses=losses,
                        edges=edges)
                    loss = sum(loss_list)

                scaled = scaler.scale(loss)  # scale the loss
                scaled.backward()  # do backward
<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
                if isinstance(optimizer, fleet.Fleet):
=======
                if isinstance(optimizer, paddle.distributed.fleet.Fleet):
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
                if isinstance(optimizer, fleet.Fleet):
>>>>>>> PaddlePaddle-release/2.4
                    scaler.minimize(optimizer.user_defined_optimizer, scaled)
                else:
                    scaler.minimize(optimizer, scaled)  # update parameters
            else:
                if nranks > 1:
<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
=======
>>>>>>> PaddlePaddle-release/2.4
                    s_logits_list, t_logits_list, feature_distill_loss = ddp_distill_model(
                        images)
                else:
                    s_logits_list, t_logits_list, feature_distill_loss = distill_model(
                        images)

                out_loss_list = loss_computation(
                    logits_list=s_logits_list,
                    labels=labels,
                    losses=losses,
                    edges=edges)
                out_loss = sum(out_loss_list)

                out_distill_loss_list = distill_loss_computation(
                    student_logits_list=s_logits_list,
                    teacher_logits_list=t_logits_list,
                    labels=labels,
                    losses=distill_losses,
                    edges=edges)
                out_distill_loss = sum(out_distill_loss_list)

                loss = out_loss + out_distill_loss + feature_distill_loss
<<<<<<< HEAD
=======
                    logits_list = ddp_model(images)
                else:
                    logits_list = model(images)
                loss_list = loss_computation(
                    logits_list=logits_list,
                    labels=labels,
                    losses=losses,
                    edges=edges)
                loss = sum(loss_list)
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
>>>>>>> PaddlePaddle-release/2.4
                loss.backward()
                optimizer.step()

            lr = optimizer.get_lr()

            # update lr
<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
            if isinstance(optimizer, fleet.Fleet):
=======
            if isinstance(optimizer, paddle.distributed.fleet.Fleet):
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
            if isinstance(optimizer, fleet.Fleet):
>>>>>>> PaddlePaddle-release/2.4
                lr_sche = optimizer.user_defined_optimizer._learning_rate
            else:
                lr_sche = optimizer._learning_rate
            if isinstance(lr_sche, paddle.optimizer.lr.LRScheduler):
                lr_sche.step()

<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
            distill_model.clear_gradients()
=======
            train_profiler.add_profiler_step(profiler_options)

            model.clear_gradients()
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
            distill_model.clear_gradients()
>>>>>>> PaddlePaddle-release/2.4
            avg_loss += loss.numpy()[0]
            avg_out_loss += out_loss.numpy()[0]
            avg_out_distill_loss += out_distill_loss.numpy()[0]
            avg_feature_distill_loss += feature_distill_loss.numpy()[0]
            if not avg_out_loss_list:
                avg_out_loss_list = [l.numpy() for l in out_loss_list]
            else:
                for i in range(len(out_loss_list)):
                    avg_out_loss_list[i] += out_loss_list[i].numpy()
            batch_cost_averager.record(
                time.time() - batch_start, num_samples=batch_size)

            if (iter) % log_iters == 0 and local_rank == 0:
                avg_loss /= log_iters
                avg_out_loss /= log_iters
                avg_out_distill_loss /= log_iters
                avg_feature_distill_loss /= log_iters
                avg_out_loss_list = [
                    l[0] / log_iters for l in avg_out_loss_list
                ]
                remain_iters = iters - iter
                avg_train_batch_cost = batch_cost_averager.get_average()
                avg_train_reader_cost = reader_cost_averager.get_average()
                eta = calculate_eta(remain_iters, avg_train_batch_cost)
                logger.info(
                    "[TRAIN] epoch: {}, iter: {}/{}, loss: {:.4f},  out_loss: {:.4f}, out_distill_loss: {:.4f}, feature_distill_loss: {:.4f}, lr: {:.6f}, batch_cost: {:.4f}, reader_cost: {:.5f}, ips: {:.4f} samples/sec | ETA {}"
                    .format((iter - 1) // iters_per_epoch + 1, iter, iters,
                            avg_loss, avg_out_loss, avg_out_distill_loss,
                            avg_feature_distill_loss, lr, avg_train_batch_cost,
                            avg_train_reader_cost,
                            batch_cost_averager.get_ips_average(), eta))
                if use_vdl:
                    log_writer.add_scalar('Train/loss', avg_loss, iter)
                    # Record all losses if there are more than 2 losses.
                    if len(avg_out_loss_list) > 1:
                        avg_loss_dict = {}
                        for i, value in enumerate(avg_out_loss_list):
                            avg_loss_dict['loss_' + str(i)] = value
                        for key, value in avg_loss_dict.items():
                            log_tag = 'Train/' + key
                            log_writer.add_scalar(log_tag, value, iter)

                    log_writer.add_scalar('Train/lr', lr, iter)
                    log_writer.add_scalar('Train/batch_cost',
                                          avg_train_batch_cost, iter)
                    log_writer.add_scalar('Train/reader_cost',
                                          avg_train_reader_cost, iter)
                avg_loss = 0.0
                avg_out_loss = 0.0
                avg_out_distill_loss = 0.0
                avg_feature_distill_loss = 0.0
                avg_out_loss_list = []
                reader_cost_averager.reset()
                batch_cost_averager.reset()

            if (iter % save_interval == 0
                    or iter == iters) and (val_dataset is not None):
                num_workers = 1 if num_workers > 0 else 0

                if test_config is None:
                    test_config = {}

<<<<<<< HEAD
<<<<<<< HEAD:slim/distill/distill_utils.py
=======
>>>>>>> PaddlePaddle-release/2.4
                mean_iou, acc, _, _, _ = evaluate(
                    student_model,
                    val_dataset,
                    num_workers=num_workers,
                    **test_config)

                student_model.train()
<<<<<<< HEAD
=======
                acc, fp, fn = evaluate(
                    model,
                    val_dataset,
                    num_workers=num_workers,
                    save_dir=save_dir,
                    **test_config)

                model.train()
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======
>>>>>>> PaddlePaddle-release/2.4

            if (iter % save_interval == 0 or iter == iters) and local_rank == 0:
                current_save_dir = os.path.join(save_dir,
                                                "iter_{}".format(iter))
                if not os.path.isdir(current_save_dir):
                    os.makedirs(current_save_dir)
                paddle.save(student_model.state_dict(),
                            os.path.join(current_save_dir, 'model.pdparams'))
                paddle.save(optimizer.state_dict(),
                            os.path.join(current_save_dir, 'model.pdopt'))
                save_models.append(current_save_dir)
                if len(save_models) > keep_checkpoint_max > 0:
                    model_to_remove = save_models.popleft()
                    shutil.rmtree(model_to_remove)

                if val_dataset is not None:
<<<<<<< HEAD
                    if acc > best_acc:
                        best_acc = acc
=======
                    if mean_iou > best_mean_iou:
                        best_mean_iou = mean_iou
>>>>>>> PaddlePaddle-release/2.4
                        best_model_iter = iter
                        best_model_dir = os.path.join(save_dir, "best_model")
                        paddle.save(
                            student_model.state_dict(),
                            os.path.join(best_model_dir, 'model.pdparams'))
                    logger.info(
<<<<<<< HEAD
                        '[EVAL] The model with the best validation Acc ({:.4f}) was saved at iter {}.'
                        .format(best_acc, best_model_iter))

                    if use_vdl:
<<<<<<< HEAD:slim/distill/distill_utils.py
                        log_writer.add_scalar('Evaluate/mIoU', mean_iou, iter)
=======
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
                        log_writer.add_scalar('Evaluate/Acc', acc, iter)
                        log_writer.add_scalar('Evaluate/Fp', fp, iter)
                        log_writer.add_scalar('Evaluate/Fn', fn, iter)
=======
                        '[EVAL] The model with the best validation mIoU ({:.4f}) was saved at iter {}.'
                        .format(best_mean_iou, best_model_iter))

                    if use_vdl:
                        log_writer.add_scalar('Evaluate/mIoU', mean_iou, iter)
                        log_writer.add_scalar('Evaluate/Acc', acc, iter)
>>>>>>> PaddlePaddle-release/2.4
            batch_start = time.time()

    # Calculate flops.
    if local_rank == 0:
<<<<<<< HEAD
        _, c, h, w = images.shape
<<<<<<< HEAD:slim/distill/distill_utils.py
        flops = paddle.flops(
            student_model, [1, c, h, w],
            custom_ops={paddle.nn.SyncBatchNorm: count_syncbn})
=======
        _ = paddle.flops(
            model, [1, c, h, w],
            custom_ops={paddle.nn.SyncBatchNorm: op_flops_funs.count_syncbn})
>>>>>>> PaddlePaddle-release/2.4:contrib/LaneSeg/core/train.py
=======

        def count_syncbn(m, x, y):
            x = x[0]
            nelements = x.numel()
            m.total_ops += int(2 * nelements)

        _, c, h, w = images.shape
        flops = paddle.flops(
            student_model, [1, c, h, w],
            custom_ops={paddle.nn.SyncBatchNorm: count_syncbn})
>>>>>>> PaddlePaddle-release/2.4

    # Sleep for half a second to let dataloader release resources.
    time.sleep(0.5)
    if use_vdl:
        log_writer.close()
